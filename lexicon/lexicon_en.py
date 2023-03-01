LEXICON_EN: dict[str, str] = {
    # Commands
    "/start": (
        "<b>What is this test for?</b>\n\n"
        "This test will help you evaluate your physical fitness"
        " and find out if you could pass a fitness test at the"
        " FBI Academy.\n\n"
        "FBI recruits take this test to become FBI agents. PFT consists"
        " of five events: sit-ups, sprint, push-ups, running, pull-ups.\n\n"
        "<b>Let's meet and get started... Choose your sex:</b>"
    ),
    "/info": (
        "The FBI Physical Fitness Test consists of five components:\n\n"
        "1. <b>Maximum Sit-ups:</b> The test-taker must perform as many"
        " sit-ups as possible in one minute.\n\n"
        "2. <b>300-Meter Sprint:</b> The test-taker must complete the"
        " 300-meter sprint as quickly as possible.\n\n"
        "3. <b>Maximum Push-ups:</b> The test-taker must perform as many"
        " push-ups as possible wihtout pauses (unlimited time).\n\n"
        "4. <b>1.5-Mile Run:</b> The test-taker must complete the 1.5-mile"
        " run as quickly as possible.\n\n"
        "5. <b>Pull-ups:</b> The test-taker must perform as many"
        " pull-ups as possible wihtout pauses (unlimited time).\n\n"
        "Each component is scored on a points system, and the test-taker"
        " must achieve a minimum passing score in each component in order"
        " to pass the overall fitness test. "
        "The specific passing score requirements may vary based on age"
        " and gender.\n\n"
        "Score table: \\table\n\n"
        "Rules and the protocol video:\n"
        "https://youtube.com/watch?v=a1Ydgfbfmmo&si=EnSIkaIECMiOmarE"
    ),
    # Content
    "table_caption": "Scoring Table",
    "registered": "Welcome on the board, let's get started /help",
    "more_info_header": (
        "Exercises are performed alternately with a 5-minute"
        " rest between exercises. Order of execution: twisting,"
        " sprinting, push-ups, running, pull-ups."
    ),
    "more_info_page_1": (
        "<b>Sit-ups</b>\n\n"
        "• Lie on your back with your shoulder blades touching the floor,"
        " arms crossed over your chest. Bend your knees at 90 degrees with"
        " your feet on the floor.\n"
        "• Have a partner hold your feet.\n"
        "• Lift your upper body until your elbows touch your mid thigh,"
        " then return to the starting position. This is one sit-up.\n"
        "• If you pause, you forfeit the rest of the minute!\n"
    ),
    "more_info_page_2": (
        "<b>300-Meter Sprint</b>\n\n"
        "• On a 0.25-mile track, start from standing and run 300"
        " meters without stopping."
    ),
    "more_info_page_3": (
        "<b>Push-ups</b>\n\n"
        "• Start with your hands on the floor no more than two hands width"
        " beyond your shoulders, with your elbows away from your body. Your"
        " feet can be no more than 3 inches apart, with your toes touching"
        " the floor.\n"
        "• As you bend your arms and lower into your push-up, your upper"
        " arms should be parallel with the floor.\n"
        "• Return to start and immediately begin the next rep.\n"
        "• If you pause, you’re done!"
    ),
    "more_info_page_4": (
        "<b>1.5-Mile Run</b>\n\n"
        "• On a 0.25-mile track, start from a standing position and run"
        " six laps."
    ),
    "more_info_page_5": (
        "<b>Pull-ups</b>\n\n"
        "• Hang from a horizontal bar, with hands at least shoulder width"
        " (but no more than 23 inches part). Palms must be turned away from"
        " your face, with arms fully extended.\n"
        "• Pull your body upward, until your chin is higher than the bar."
        " (No swinging or jerking!)\n"
        "• Lower back to the hanging position. This is one pull-up.\n"
        "• If you pause, you’re done."
    ),
    "test_result": (
        "<b>Test result</b>\n\n"
        "Sit-ups: {situps}\n"
        "Sprint: {sprint}\n"
        "Push-ups: {pushups}\n"
        "Running: {running}\n"
        "Pull-ups: {pullups}\n\n"
        "<b>Score:</b> {score}"
    ),
    "continue_pressed": "Continue...",
    "result_saved": "Result is successfully saved.",
    # Buttons
    "btn_male": "Male",
    "btn_female": "Female",
    "btn_more_info": "More information",
    "btn_result_save": "Save",
    "btn_result_continue": "Continue",
    # Forms
    "test_result_form_header": "Let's calculate your result, fill the data...",
    "test_result_form_situps": "How many sit-ups did you do?",
    "test_result_form_sprint": "How long did you run 300 meters?",
    "test_result_form_pushups": "How many push-ups did you do?",
    "test_result_form_running": "How long did you run 1.5 miles?",
    "test_result_form_pullups": "How many pull-ups did you do?",
    # Warnings
    "start_warning": "You have already started me. /help",
    "sex_warning": "Please select your sex to get started.",
    "sex_pressed_warning": "You have already choosen sex. /help",
    "result_save_continue_warning": "You should save result or press continue.",
    # Validation
    "repetition_not_integer": "You should write a positive number...",
    "wrong_seconds_format": (
        "Write the value in following format:\n'01:23' (sec:ms)\n"
    ),
    "wrong_milliseconds_format": (
        "Write the value in following format:\n'1.23' (sec.ms)\n"
    ),
}
