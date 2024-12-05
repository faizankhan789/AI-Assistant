import google.generativeai as genai


def get_response(user_input):
    genai.configure(api_key="AIzaSyAn726Chm0tAhjqxfNEg3R125bvbPk_Iu8")
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Include a system message to instruct the bot on its behavior
    system_message = "you are ai assisstant"

    # Prepend the system message to the user's input
    final_input = system_message + "\n" + user_input

    response = model.generate_content(final_input)
    return response.text
