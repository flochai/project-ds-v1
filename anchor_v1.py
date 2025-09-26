import streamlit as st
from datetime import datetime
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="Anchor Method Scheduler", page_icon="⚓", layout="centered")
st.title("⚓ Anchor Method Generator")

with st.form("schedule_form"):
    lesson = st.text_input("Lesson / Topic name", placeholder="e.g., VPC & Subnets")
    base_date = st.date_input("First study date (Day 0)", value=datetime.today().date())
    extended = st.toggle("Extended Anchors (3 mo, 6 mo, 1 yr)")
    submitted = st.form_submit_button("Generate dates")

if submitted:
    if not lesson.strip():
        st.warning("Please enter a lesson name.")
    else:
        base_dt = datetime.combine(base_date, datetime.min.time())
        anchors = [
            ("Day 0", base_dt),
            ("+3 days", base_dt + relativedelta(days=+3)),
            ("+7 days", base_dt + relativedelta(days=+7)),
            ("+14 days", base_dt + relativedelta(days=+14)),
            ("+30 days", base_dt + relativedelta(days=+30)),
        ]
        if extended:
            anchors += [
                ("+3 months", base_dt + relativedelta(months=+3)),
                ("+6 months", base_dt + relativedelta(months=+6)),
                ("+1 year",  base_dt + relativedelta(years=+1)),
            ]

        st.subheader(f"Schedule for: **{lesson}**")
        st.table(
            [{"Anchor": label, "Date": dt.strftime("%Y-%m-%d (%a)")} for label, dt in anchors]
        )

        st.download_button(
            label="Download as .txt",
            data="\n".join([f"{label}: {dt.strftime('%Y-%m-%d (%a)')}" for label, dt in anchors]),
            file_name=f"{lesson.replace(' ', '_')}_anchors.txt",
            mime="text/plain",
        )

        #ICS export
        def to_ics(entries):
            def ics_dt(d): return d.strftime("%Y%m%d")
            lines = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Anchor Method//EN"]
            for label, dt in entries:
                # All-day events; adjust if you want timed reminders
                lines += [
                    "BEGIN:VEVENT",
                    f"UID:{lesson}-{label}-{ics_dt(dt)}@anchor-method",
                    f"DTSTAMP:{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}",
                    f"DTSTART;VALUE=DATE:{ics_dt(dt)}",
                    f"SUMMARY:{lesson} — {label}",
                    "END:VEVENT",
                ]
            lines.append("END:VCALENDAR")
            return "\n".join(lines)

        st.download_button(
            label="Download Calendar (.ics)",
            data=to_ics(anchors),
            file_name=f"{lesson.replace(' ', '_')}_anchors.ics",
            mime="text/calendar",
        )
