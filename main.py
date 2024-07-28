from plyer import notification

title = "Please drink water "
message = "Drinking water helps maintain the balance of bodily fluids, essential for digestion, circulation, and temperature regulation."
app_name = "My App"  # Optional: Name of the app generating the notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title=title,
            message=message,
            app_name=app_name,
            timeout=10,
            app_icon="C:\\Users\\Devang\\PycharmProjects\\drinknotification\\glass-with-water_icon-icons.com_70479.ico"  # Escape backslashes
        )
    time.sleep(60*60)