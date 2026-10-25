# Student Performance AI

A Streamlit demonstration app that estimates a math score and identifies areas
where a student may benefit from academic support. The included models use
synthetic training data; their predictions are not validated real-world risk
estimates and should not be used in place of educator judgment.

## Run locally

Use Python 3.11 or later, then install the dependencies and start Streamlit:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

The three model files must remain alongside `app.py`:

- `math_score_model.pkl`
- `academic_support_model.pkl`
- `subject_support_models.pkl`

## Deploy on Streamlit Community Cloud

After this repository is published, create a new app in Streamlit Community
Cloud, select this repository and branch, and set the main file path to
`app.py`. The dependency list is in `requirements.txt`.
