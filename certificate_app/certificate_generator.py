import cv2
from django.utils.dateformat import format



def get_day_month_year(date_value):
    day = date_value.day
    month = date_value.month
    year = str(date_value.year)

    day_formatted = f"{day}{ 'th' if 11 <= day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')}"
    month_formatted = format(date_value, 'F')
    
    return day_formatted, month_formatted, year



def update_certificate_template(template_image, user_data):
    # Make a copy of the template to work on
    template = template_image.copy()

    # Resize the image
    zoom_factor = 0.5  # Example zoom factor of 0.5 (50% zoom out)
    updated_template = cv2.resize(template, None, fx=zoom_factor, fy=zoom_factor)
    
    name_coords = (265,339)  
    location_coords = (305,462)  
    death_day_coords,death_month_coords,death_year_coords = (339,394),(536,391),(812,395)
    birth_day_coords,birth_month_coords,birth_year_coords = (391,523),(573,521),(847,527)

    user_name = user_data['full_name']
    location = user_data['death_location']
    death_day,death_month,death_year = get_day_month_year(user_data['death_date'])
    print(death_day)
    birth_day,birth_month,birth_year = get_day_month_year(user_data['date_of_birth'])

    # Define the font, color, and size for the text to be added
    def draw_text(text,coords):
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX #FONT_HERSHEY_DUPLEX #FONT_HERSHEY_SCRIPT_SIMPLEX #FONT_HERSHEY_SIMPLEX
        font_color = (0, 0, 0)  # Black color (BGR format)
        font_scale = 1
        thickness = 1
        line_type=cv2.LINE_AA

        cv2.putText(updated_template, text, coords, font, font_scale, font_color, thickness, lineType=line_type)

    # Add the user's name and date to the updated_template
    draw_text(user_name,name_coords)
    draw_text(location,location_coords)
    draw_text(death_day,death_day_coords)
    draw_text(death_month,death_month_coords)
    draw_text(death_year,death_year_coords)
    draw_text(birth_day,birth_day_coords)
    draw_text(birth_month,birth_month_coords)
    draw_text(birth_year,birth_year_coords)

    return updated_template

