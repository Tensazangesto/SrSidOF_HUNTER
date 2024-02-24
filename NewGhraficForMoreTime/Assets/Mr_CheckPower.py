from plyer import notification
import psutil


def check_battery_status(battery, plugged):
    if plugged:
        percent = battery.percent
        if percent <= 80:
            notification.notify(

                title="Charger Plugged In",
                message=" To get the better battery life, charge upto 80%",
                app_name="MoreTime",
                app_icon="assets\\clock.ico",
                timeout=2
            )

        elif percent == 100:
            notification.notify(
                title="Charger Plugged In",
                message=" Please plugged out the charger. Battery is charged",
                app_name="MoreTime",
                app_icon="assets\\clock.ico",
                timeout=2
            )

        else:
            notification.notify(
                title="Charger Plugged In",
                message=" Remove the charger please. For better battery life charge up to 80%",
                app_name="MoreTime",
                app_icon="assets\\clock.ico",
                timeout=2
            )

    else:
        percent = battery.percent
        if percent <= 20:
            notification.notify(
                title="Battery Reminder",
                message="Your battery is running low. You might want to plug in your PC ",
                app_name="MoreTime",
                app_icon="assets\\clock.ico",
                timeout=2
            )

        elif percent <= 50:
            notification.notify(
                title="Battery Reminder",
                message=f" Battery is {percent}.",
                app_name="MoreTime",
                app_icon="assets\\clock.ico",
                timeout=2
            )

        elif percent == 100:
            notification.notify(
                title="Battery Reminder",
                message="Your System is Fully charged",
                app_name="MoreTime",
                app_icon="assets\\clock.ico",
                timeout=2
            )

        else:
            notification.notify(
                title="Battery Reminder",
                message=f"Battery is {percent}",
                app_name="MoreTime",
                app_icon="assets\\clock.ico",
                timeout=2
            )


while 1:
    from time import sleep
    sleep(30)
    battery = psutil.sensors_battery()

    plugged = battery.power_plugged

    print(check_battery_status(battery, plugged))