import streamlit as st
import pandas as pd

# Create a DataFrame to store reported litter locations
reported_locations = pd.DataFrame(columns=["Location Name", "Description", "Latitude", "Longitude"])

# Create a Streamlit sidebar for reporting litter
st.sidebar.title("Report Litter")
location_name = st.sidebar.text_input("Location Name")
description = st.sidebar.text_area("Description")
latitude = st.sidebar.number_input("Latitude", min_value=-90.0, max_value=90.0)
longitude = st.sidebar.number_input("Longitude", min_value=-180.0, max_value=180.0)

if st.sidebar.button("Submit Report"):
    if location_name and description and latitude and longitude:
        reported_locations = reported_locations.append(
            {"Location Name": location_name, "Description": description, "Latitude": latitude, "Longitude": longitude},
            ignore_index=True,
        )
        st.sidebar.success("Litter location reported successfully!")

# Create a Streamlit main content for locating and cleaning litter
st.title("Litter Locator")
st.markdown(
    "Welcome to Litter Locator! You can report litter locations on the left sidebar, and cleaning teams can use this page to find and clean these places."
)

# Display a map of reported litter locations
st.map(reported_locations)

# Create a search form for cleaning teams
st.header("Search Litter Locations")
search_latitude = st.number_input("Search Latitude", min_value=-90.0, max_value=90.0)
search_longitude = st.number_input("Search Longitude", min_value=-180.0, max_value=180.0)
search_radius = st.slider("Search Radius (miles)", min_value=1, max_value=100, step=1, value=10)

if st.button("Search"):
    # Filter reported locations within the search radius
    filtered_locations = reported_locations.copy()
    filtered_locations["Distance"] = filtered_locations.apply(
        lambda row: (
            (search_latitude - row["Latitude"]) ** 2 + (search_longitude - row["Longitude"]) ** 2
        ) ** 0.5,
        axis=1,
    )
    filtered_locations = filtered_locations[filtered_locations["Distance"] <= (search_radius / 69)]  # Approximate miles to degrees conversion

    # Display filtered locations
    if not filtered_locations.empty:
        st.success("Found litter locations within the search radius:")
        st.map(filtered_locations)
        st.table(filtered_locations.drop(columns="Distance"))
    else:
        st.warning("No litter locations found within the search radius.")

# Note: You can add more functionality like user authentication, data persistence, and more as needed.


Note: You can further customize the layout and appearance of the app as needed.
