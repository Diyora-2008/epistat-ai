
import math
import streamlit as st

st.set_page_config(
    page_title="EpiStat AI",
    page_icon="📊",
    layout="centered"
)

st.title("📊 EpiStat AI")
st.subheader("AI in Biostatistics")
st.write(
    "An interactive tool for epidemiological data analysis."
)

st.info(
    "Educational prototype. Use synthetic or approved "
    "aggregate data only. This is not a diagnostic tool."
)

tab1, tab2, tab3 = st.tabs([
    "📈 Analysis", "📚 Learn", "🔒 Privacy"
])

with tab1:
    st.header("Prevalence calculator")

    population = st.text_input(
        "Study population",
        "Adults screened"
    )

    n = st.number_input(
        "Total sample size",
        min_value=1,
        value=200,
        step=1
    )

    x = st.number_input(
        "Number of cases",
        min_value=0,
        max_value=int(n),
        value=min(24, int(n)),
        step=1
    )

    if st.button("Calculate results", type="primary"):
        p = x / n
        z = 1.96
        den = 1 + z**2 / n
        center = (p + z**2 / (2*n)) / den
        margin = z * math.sqrt(
            p*(1-p)/n + z**2/(4*n**2)
        ) / den

        low = max(0, center - margin)
        high = min(1, center + margin)

        st.metric("Prevalence", f"{p:.1%}")
        st.metric(
            "95% Wilson confidence interval",
            f"{low:.1%} – {high:.1%}"
        )

        st.write(f"Population: {population}")
        st.write(f"Cases: {x} out of {n}")

        st.subheader("Interpretation")
        st.write(
            f"The estimated prevalence is {p:.1%}. "
            f"The 95% Wilson confidence interval is "
            f"{low:.1%} to {high:.1%}."
        )

        st.bar_chart({
            "Prevalence (%)": [p * 100],
            "Lower CI (%)": [low * 100],
            "Upper CI (%)": [high * 100]
        })

with tab2:
    st.header("Learn biostatistics")
    st.latex(r"\text{Prevalence}=\frac{x}{n}\times100\%")
    st.write(
        "Prevalence is the proportion of a defined "
        "population with a condition at a specified time."
    )
    st.write(
        "A confidence interval describes uncertainty "
        "around an estimate. It does not eliminate bias."
    )

with tab3:
    st.header("Privacy and ethics")
    st.write(
        "- Do not enter patient names or identifiers.\n"
        "- Use synthetic or approved aggregate data.\n"
        "- This prototype does not require patient records.\n"
        "- No external AI service is connected.\n"
        "- Verify findings before research use."
    )

st.caption(
    "EpiStat AI | Educational prototype | "
    "Not for clinical diagnosis"
)
