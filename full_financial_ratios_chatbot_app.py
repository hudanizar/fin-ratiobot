
import streamlit as st

st.set_page_config(page_title="Financial Ratio Tutor", layout="centered")
st.title("📊 Financial Ratio Tutor Chatbot")

# Sidebar Navigation
st.sidebar.header("📚 Modules")
module = st.sidebar.selectbox(
    "Choose a module to explore:",
    [
        "Module 1: Liquidity Ratios",
        "Module 2: Capital Structure Ratios",
        "Module 3: Profitability Ratios",
        "Module 4: Market Value Ratios",
        "Module 5: Dividend-Based Ratios"
    ]
)

# Ratio content bank
modules = {
    "Module 1: Liquidity Ratios": {
        "Current Ratio": {
            "formula_en": "Current Ratio = Current Assets ÷ Current Liabilities",
            "formula_my": "Nisbah Semasa = Aset Semasa ÷ Liabiliti Semasa",
            "meaning": "Measures a firm's ability to pay short-term obligations using current assets.",
            "example": "Current Assets = RM100,000, Liabilities = RM50,000 → Ratio = 2.0",
            "quiz": ("Assets = RM60,000, Liabilities = RM30,000. Ratio?", "2.0")
        },
        "Quick Ratio": {
            "formula_en": "Quick Ratio = (Current Assets − Inventories) ÷ Current Liabilities",
            "formula_my": "Nisbah Pantas = (Aset Semasa − Inventori) ÷ Liabiliti Semasa",
            "meaning": "Measures liquidity excluding inventory.",
            "example": "Assets = RM90,000, Inventory = RM30,000, Liabilities = RM60,000 → Ratio = 1.0",
            "quiz": ("Assets = RM80k, Inventory = RM20k, Liabilities = RM40k. Ratio?", "1.5")
        }
    },
    "Module 2: Capital Structure Ratios": {
        "Debt-to-Equity": {
            "formula_en": "D/E = Total Liabilities ÷ Shareholders’ Equity",
            "formula_my": "Nisbah Hutang kepada Ekuiti = Jumlah Liabiliti ÷ Ekuiti Pemegang Saham",
            "meaning": "Shows financial leverage—how much debt per RM1 of equity.",
            "example": "Liabilities = RM300k, Equity = RM200k → Ratio = 1.5",
            "quiz": ("Liabilities = RM400k, Equity = RM250k. Ratio?", "1.6")
        }
    },
    "Module 3: Profitability Ratios": {
        "ROE": {
            "formula_en": "ROE = Net Income ÷ Shareholders’ Equity × 100%",
            "formula_my": "Pulangan atas Ekuiti = Pendapatan Bersih ÷ Ekuiti × 100%",
            "meaning": "Measures return generated on equity investment.",
            "example": "Net Income = RM50k, Equity = RM250k → ROE = 20%",
            "quiz": ("Income = RM80k, Equity = RM400k. ROE?", "20%")
        },
        "ROA": {
            "formula_en": "ROA = Net Income ÷ Total Assets × 100%",
            "formula_my": "Pulangan atas Aset = Pendapatan Bersih ÷ Jumlah Aset × 100%",
            "meaning": "Measures overall asset efficiency in generating profits.",
            "example": "Income = RM40k, Assets = RM500k → ROA = 8%",
            "quiz": ("Income = RM75k, Assets = RM600k. ROA?", "12.5%")
        }
    },
    "Module 4: Market Value Ratios": {
        "P/E Ratio": {
            "formula_en": "P/E = Market Price ÷ EPS",
            "formula_my": "Nisbah Harga kepada Pendapatan = Harga Saham ÷ Pendapatan Sesaham",
            "meaning": "Shows how much investors pay per RM1 of earnings.",
            "example": "Price = RM20, EPS = RM2 → P/E = 10",
            "quiz": ("Price = RM50, EPS = RM1.25. P/E?", "40")
        }
    },
    "Module 5: Dividend-Based Ratios": {
        "Dividend Yield": {
            "formula_en": "Yield = Annual DPS ÷ Price × 100%",
            "formula_my": "Hasil Dividen = Dividen Tahunan ÷ Harga Saham × 100%",
            "meaning": "Annual return from dividends per RM invested.",
            "example": "DPS = RM1, Price = RM25 → Yield = 4%",
            "quiz": ("DPS = RM1.20, Price = RM30. Yield?", "4%")
        }
    }
}

# Load selected module
selected_ratios = modules.get(module, {})

# User chooses a ratio
ratio = st.selectbox("Select a ratio to learn:", list(selected_ratios.keys()))
info = selected_ratios[ratio]

# Display content
st.subheader("🧠 Formula")
st.markdown(f"**English:** {info['formula_en']}")
st.markdown(f"**Malay:** {info['formula_my']}")

st.subheader("💡 Meaning")
st.write(info["meaning"])

st.subheader("🧮 Example")
st.write(info["example"])

# Quiz section
st.subheader("📝 Quiz Yourself")
q, correct = info["quiz"]
user_answer = st.text_input(q)

if user_answer:
    if user_answer.strip() == correct:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. Correct answer: {correct}")
