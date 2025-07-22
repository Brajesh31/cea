import streamlit as st

def candidate_elimination(examples):
    specific_h = examples[0][:-1]
    general_h = [["?" for _ in range(len(specific_h))] for _ in range(len(specific_h))]
    
    for example in examples:
        if example[-1] == "Yes":
            for i in range(len(specific_h)):
                if example[i] != specific_h[i]:
                    specific_h[i] = "?"
                    general_h[i][i] = "?"
        else:
            for i in range(len(specific_h)):
                if example[i] != specific_h[i]:
                    general_h[i][i] = specific_h[i]
                else:
                    general_h[i][i] = "?"
                    
    return specific_h, general_h

def main():
    st.title("Candidate Elimination Algorithm")
    st.write("Enter examples in the form of weather conditions (Outlook, Temperature, Humidity, Windy) and the corresponding sport decision (Yes/No).")

    examples = st.text_area("Enter examples separated by newline", "Sunny, Hot, High, False, No\nSunny, Hot, High, True, No\nOvercast, Hot, High, False, Yes\nRain, Mild, High, False, Yes\nRain, Cool, Normal, False, Yes\nRain, Cool, Normal, True, No\nOvercast, Cool, Normal, True, Yes\nSunny, Mild, High, False, No\nSunny, Cool, Normal, False, Yes\nRain, Mild, Normal, False, Yes\nSunny, Mild, Normal, True, Yes\nOvercast, Mild, High, True, Yes\nOvercast, Hot, Normal, False, Yes\nRain, Mild, High, True, No")
    examples = [example.strip().split(", ") for example in examples.split("\n")]

    if st.button("Run Algorithm"):
        specific_h, general_h = candidate_elimination(examples)
        
        st.subheader("Specific Hypothesis:")
        st.write(specific_h)

        st.subheader("General Hypothesis:")
        for hypothesis in general_h:
            st.write(hypothesis)

if __name__ == "__main__":
    main()
