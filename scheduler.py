from apscheduler.schedulers.blocking import BlockingScheduler

def your_task():
    # Replace this function with the task you want to run every 5 minutes
    print("This task runs every 1 minute!")

if __name__ == "__main__":
    # Create an instance of the scheduler
    scheduler = BlockingScheduler()

    # Schedule the task to run every 1 minute
    scheduler.add_job(your_task, 'interval', minutes=1)

    try:
        # Start the scheduler
        print("Script is running. Press Ctrl+C to exit.")
        scheduler.start()
    except KeyboardInterrupt:
        # Catch Ctrl+C and stop the scheduler gracefully
        print("Scheduler stopped.")