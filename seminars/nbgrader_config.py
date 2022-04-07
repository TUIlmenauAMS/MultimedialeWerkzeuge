#According to: https://nbgrader.readthedocs.io/en/stable/user_guide/managing_assignment_files.html#setting-up-the-exchange
#Gerald Schuller, March 2022

c = get_config()

c.CourseDirectory.course_id = "MMW" # Don't change this
c.CourseDirectory.student_id = "12345" # Replace by your Matrikel Number
c.Exchange.root = "/home/fera/SS2022_Seminars/TUI_Nextcloud" # Replace by your shared folder path

