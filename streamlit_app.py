import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# Function to calculate holiday dates
def get_dates(year, day_type):
    dates = []

    # Helper functions to calculate specific dates
    def nth_weekday_in_month(year, month, weekday, n):
        first_day_of_month = datetime(year, month, 1)
        first_weekday = first_day_of_month + timedelta(days=(weekday - first_day_of_month.weekday() + 7) % 7)
        return first_weekday + timedelta(weeks=n-1)

    def third_sunday_in_june(year):
        return nth_weekday_in_month(year, 6, 6, 3)

    def first_sunday_in_september(year):
        return nth_weekday_in_month(year, 9, 6, 1)

    def second_sunday_in_august(year):
        return nth_weekday_in_month(year, 8, 6, 2)

    def ascension_day(year):
        easter_sunday = easter(year)
        return easter_sunday + timedelta(days=39)

    def march_19(year):
        return datetime(year, 3, 19)

    def second_sunday_in_november(year):
        return nth_weekday_in_month(year, 11, 6, 2)

    def december_5(year):
        return datetime(year, 12, 5)

    def february_23(year):
        return datetime(year, 2, 23)

    def second_sunday_in_june(year):
        return nth_weekday_in_month(year, 6, 6, 2)

    def june_20(year):
        return datetime(year, 6, 20)

    def june_5(year):
        return datetime(year, 6, 5)

    def june_21(year):
        return datetime(year, 6, 21)

    def november_12(year):
        return datetime(year, 11, 12)

    def march_11(year):
        return datetime(year, 3, 11)

    def first_sunday_in_june(year):
        return nth_weekday_in_month(year, 6, 6, 1)

    def june_23(year):
        return datetime(year, 6, 23)

    def second_sunday_in_may(year):
        return nth_weekday_in_month(year, 5, 6, 2)

    def first_sunday_in_may(year):
        return nth_weekday_in_month(year, 5, 6, 1)

    def may_8(year):
        return datetime(year, 5, 8)

    def august_8(year):
        return datetime(year, 8, 8)

    def easter(year):
        "Returns Easter as a date object."
        a = year % 19
        b = year // 100
        c = year % 100
        d = b // 4
        e = b % 4
        f = (b + 8) // 25
        g = (b - f + 1) // 3
        h = (19 * a + b - d - g + 15) % 30
        i = c // 4
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = (a + 11 * h + 22 * l) // 451
        month = (h + l - 7 * m + 114) // 31
        day = ((h + l - 7 * m + 114) % 31) + 1
        return datetime(year, month, day)

    if day_type == "Father's":
        # Calculate Father's Day dates for the given year
        dates.append(["🇺🇸 🇨🇦 🇬🇧 🇦🇷 🇮🇳 🇯🇵 🇰🇿 🇲🇽 🇳🇱 🇵🇰 🇵🇭 🇿🇦 🇱🇰 🇹🇷 🇻🇪", third_sunday_in_june(year)])
        dates.append(["🇦🇺 🇳🇿", first_sunday_in_september(year)])
        dates.append(["🇧🇷", second_sunday_in_august(year)])
        dates.append(["🇩🇪", ascension_day(year)])
        dates.append(["🇪🇸 🇮🇹 🇧🇪 (Antwerp) 🇵🇹", march_19(year)])
        dates.append(["🇸🇪 🇫🇮 🇳🇴 🇪🇪", second_sunday_in_november(year)])
        dates.append(["🇹🇭", december_5(year)])
        dates.append(["🇷🇺", february_23(year)])
        dates.append(["🇧🇪 (excluding Antwerp)", second_sunday_in_june(year)])
        dates.append(["🇧🇬", june_20(year)])
        dates.append(["🇩🇰", june_5(year)])
        dates.append(["🇪🇬 🇯🇴 🇱🇧 🇸🇾 🇦🇪", june_21(year)])
        dates.append(["🇮🇩", november_12(year)])
        dates.append(["🇮🇷", march_11(year)])
        dates.append(["🇱🇹 🇨🇭", first_sunday_in_june(year)])
        dates.append(["🇵🇱", june_23(year)])
        dates.append(["🇷🇴", second_sunday_in_may(year)])
        dates.append(["🇹🇼", august_8(year)])
    elif day_type == "Mother's":
        # Calculate Mother's Day dates for the given year
        dates.append(["🇺🇸 🇨🇦 🇦🇺 🇳🇿 🇩🇰 🇮🇳 🇮🇹 🇯🇵 🇨🇭 🇧🇪 (excluding Antwerp) 🇧🇷 🇫🇮 🇩🇪 🇳🇱 🇵🇰 🇿🇦 🇹🇷 🇵🇭 🇱🇰 🇪🇸 🇵🇹 🇸🇪 🇪🇪 🇳🇴 🇹🇼", second_sunday_in_may(year)])
        dates.append(["🇬🇧", nth_weekday_in_month(year, 3, 6, 4)])  # Fourth Sunday in Lent (Mothering Sunday)
        dates.append(["🇦🇷", nth_weekday_in_month(year, 10, 6, 3)])  # Third Sunday in October
        dates.append(["🇰🇿 🇲🇽", datetime(year, 5, 10)])  # May 10
        dates.append(["🇹🇭", datetime(year, 8, 12)])  # August 12 (Queen Sirikit's birthday)
        dates.append(["🇷🇺", nth_weekday_in_month(year, 11, 6, -1)])  # Last Sunday in November
        dates.append(["🇧🇪 (Antwerp)", datetime(year, 8, 15)])  # August 15
        dates.append(["🇧🇬 🇷🇴", datetime(year, 3, 8)])  # March 8 (International Women's Day)
        dates.append(["🇪🇬 🇯🇴 🇱🇧 🇸🇾 🇦🇪", datetime(year, 3, 21)])  # March 21 (Spring Equinox)
        dates.append(["🇮🇩", datetime(year, 12, 22)])  # December 22
        dates.append(["🇮🇷", datetime(year, 3, 18)])  # 20 Jumada al-thani (Islamic calendar, birthday of Fatimah)
        dates.append(["🇱🇹", first_sunday_in_may(year)])  # First Sunday in May
        dates.append(["🇵🇱", datetime(year, 5, 26)])  # May 26
    elif day_type == "Parent's":
        dates.append(["🇰🇷", datetime(year, 5, 8)])  # May 8 (Parents' Day)

    return dates

# Generate a calendar for the next 2 years
years = range(datetime.now().year, datetime.now().year + 2)
all_dates = []

for year in years:
    father_dates = get_dates(year, "Father's")
    mother_dates = get_dates(year, "Mother's")
    parents_dates = get_dates(year, "Parent's")
    for country, date in father_dates:
        all_dates.append([country, date.strftime("%Y-%m-%d"), "Father's Day"])
    for country, date in mother_dates:
        all_dates.append([country, date.strftime("%Y-%m-%d"), "Mother's Day"])
    for country, date in parents_dates:
        all_dates.append([country, date.strftime("%Y-%m-%d"), "Parents' Day"])
    all_dates.append(["💃", datetime(year, 3, 8).strftime("%Y-%m-%d"), "International Women's Day"])
    all_dates.append(["❤️", datetime(year, 2, 14).strftime("%Y-%m-%d"), "Valentine's Day"])

# Create a DataFrame with three columns: Countries, Dates, and Type
calendar_df = pd.DataFrame(all_dates, columns=["Countries", "Dates", "Type"])

calendar_df['Dates'] = pd.to_datetime(calendar_df['Dates'])
current_date = pd.to_datetime(datetime.now().date())
calendar_df = calendar_df[calendar_df['Dates'] >= current_date].groupby(['Countries','Type'], as_index=False).agg('min').sort_values('Dates')

# Function to calculate days left
def calculate_days_left(date):
    today = pd.to_datetime(datetime.now().date())
    days_left = (date - today).days
    if days_left < 0:  # If the date has passed for this year, calculate for next year
        days_left = (date.replace(year=date.year + 1) - today).days
    return days_left

# Calculate days left and progress
calendar_df["Days Left"] = calendar_df["Dates"].apply(calculate_days_left)
calendar_df["Progress"] = calendar_df["Days Left"].apply(lambda x: max(0, (365 - x) / 365))

# Inject CSS to make progress bars thicker
st.markdown(
    """
    <style>
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
        height: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app
st.title("Don't Forget")

for index, row in calendar_df.iterrows():
    days_left = row["Days Left"]
    progress = row["Progress"]
    
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"{row['Countries']} {row['Type']}")
    with col2:
        st.write(f"{days_left} days left")
    st.progress(progress)
