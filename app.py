import streamlit as st
from groq import Groq
import re

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title(" 🗄️ SQL Query Generator")
st.write("!جاهز SQL اكتب سؤالك بالعربي أو الإنجليزي وبيطلع لك ")

db_type = st.selectbox(":اختر قاعدة البيانات", ["MySQL", "PostgreSQL", "SQL Server", "SQLite"])
user_input = st.text_area(":وصف البيانات اللي تبغاها", placeholder="مثال: ابغى كل العملاء اللي اشتروا اكثر من مرتين")

if st.button("Generate SQL⚡"):
    if user_input:
        check = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": "Is this request related to database or SQL query? Reply with one word only: Yes or No.\nRequest: " + user_input}]
        )
        is_sql = check.choices[0].message.content.strip()

        if "No" in is_sql:
            st.warning("⚠️ Please enter a request related to SQL or databases only.")
        else:
            lang_check = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": "Is this text Arabic or English? Reply with one word only: Arabic or English. Text: " + user_input}]
            )
            language = lang_check.choices[0].message.content.strip()

            if "Arabic" in language:
                system_msg = "You are a SQL expert. Rules: 1. Explain in Modern Standard Arabic only. 2. Never put English words inside Arabic sentences. 3. Technical terms like SELECT and GROUP BY go inside backticks only. 4. Format every line as: `SQL line` : Arabic explanation only."
            else:
                system_msg = "You are a SQL expert. Explain in English only. Format every line as: `SQL line` : English explanation only. Never mix languages."

            arabic_words = re.findall(r'[\u0600-\u06FF]+', user_input)
            arabic_terms = ', '.join(arabic_words) if arabic_words else 'none'

            prompt = "Write a " + db_type + " SQL query for this request: " + user_input + "\n\nStrict rules:\n1. The SQL query must use English only for all table names, column names, and keywords.\n2. These Arabic terms must appear in the query EXACTLY as written, character by character: " + arabic_terms + "\n3. Do NOT change, translate, or modify any Arabic text.\n4. Start with the SQL code block\n5. After the SQL block, explain each line in this exact format:\n`SQL line here` : explanation here\n6. One language only for explanations"            
            
            
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response.choices[0].message.content

            if "```sql" in result:
                sql_part = result.split("```sql")[1].split("```")[0].strip()
                explanation_part = result.split("```")[-1].strip()
                cleaned = re.sub(r'[^\u0600-\u06FF\u0020-\u007E\n\r\t،؟!:.`*-]', '', explanation_part)

                st.subheader("SQL Query")
                st.code(sql_part, language="sql")

                st.subheader("الشرح")
                st.markdown(cleaned)
            else:
                st.markdown(result)
    else:
        st.warning("⚠️ اكتب وصف أولاً!")