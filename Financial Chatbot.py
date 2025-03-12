import pandas as pd

def simple_chatbot(user_query, data):
    if user_query.lower() == "what is the total revenue?":
        return f"The total revenue is {data['Total Revenue'].iloc[-1]:,.2f}."
    elif user_query.lower() == "how has net income changed over the last year?":
        change = data['Net Income'].pct_change().iloc[-1] * 100
        return f"The net income has {'increased' if change > 0 else 'decreased'} by {abs(change):.2f}% over the last year."
    elif user_query.lower() == "what are the total assets?":
        return f"The total assets amount to {data['Total Assets'].iloc[-1]:,.2f}."
    elif user_query.lower() == "what are the total liabilities?":
        return f"The total liabilities amount to {data['Total Liabilities'].iloc[-1]:,.2f}."
    elif user_query.lower() == "what is the cash flow from operating activities?":
        return f"The cash flow from operating activities is {data['Cash Flow from Operating Activities'].iloc[-1]:,.2f}."
    else:
        return "Sorry, I can only provide information on predefined queries."

if __name__ == "__main__":
    # Load the analyzed financial data (assuming it's stored in 'financial_data.csv')
    data = pd.read_csv("financial_data.csv")
    
    print("Welcome to the Financial Chatbot! Ask a predefined question or type 'exit' to quit.")
    while True:
        user_query = input("You: ")
        if user_query.lower() == "exit":
            print("Goodbye!")
            break
        response = simple_chatbot(user_query, data)
        print("Bot:", response)
