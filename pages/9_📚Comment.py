from dataclasses import asdict
from datetime import datetime
import streamlit as st
import db

st.set_page_config(layout="centered", page_icon="💬", page_title="Comment Section")

COMMENT_TEMPLATE_MD = """{} - {}
> {}"""

st.title("Comments")

st.subheader("Please leave your comment below")


def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")


#Connection with google sheets

conn = db.connect()
comments = db.collect(conn)



# Show comments

with st.expander("💬 Open comments"):

    # Show comments

    st.write("**Comments:**")

    for index, entry in enumerate(comments.itertuples()):
        st.markdown(COMMENT_TEMPLATE_MD.format(entry.name, entry.date, entry.comment))

        is_last = index == len(comments) - 1
        is_new = "just_posted" in st.session_state and is_last
        if is_new:
            st.success("☝️ Your comment was successfully posted.")

    space(2)

    # Insert comment

    st.write("**Add your own comment:**")
    form = st.form("comment")
    name = form.text_input("Name")
    comment = form.text_area("Comment")
    submit = form.form_submit_button("Add comment")

    if submit:
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        db.insert(conn, [[name, comment, date]])
        if "just_posted" not in st.session_state:
            st.session_state["just_posted"] = True
        st.experimental_rerun()