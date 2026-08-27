test:
	pytest tests/ -v

app:
	streamlit run src/aquascope_toolkit/app.py
