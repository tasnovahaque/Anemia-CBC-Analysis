# Anemia CBC Analysis

## Overview
This project analyzes Complete Blood Count (CBC) data to detect and classify anemia. It uses Python for data processing, analysis, and visualization. The goal is to provide insights into anemia types and severity using CBC parameters.

## Features
- Data preprocessing and cleaning
- Exploratory data analysis (EDA)
- Anemia detection and classification
- Visualization of CBC parameters
- Interactive Jupyter Notebook for experimentation

## Project Structure
- `app.py`: Main application script
- `CSE_303_project_final(2).ipynb`: Jupyter Notebook with analysis and visualizations
- `requirements.txt`: Python dependencies
- `CSE__303_project (4).pdf`: Project documentation

## Installation
1. Clone the repository:
	```powershell
	git clone <repo-url>
	```
2. Navigate to the project directory:
	```powershell
	cd Anemia-CBC-Analysis
	```
3. Install dependencies:
	```powershell
	pip install -r requirements.txt
	```

## Usage
- To run the main script:
  ```powershell
  python app.py
  ```
- To explore the analysis interactively, open `CSE_303_project_final(2).ipynb` in Jupyter Notebook:
  ```powershell
  jupyter notebook CSE_303_project_final(2).ipynb
  ```

## Requirements
See `requirements.txt` for the list of required Python packages.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is for educational purposes.

## Contact
For questions or feedback, please contact the project owner.

## Results & Analysis

### Model Performance

| Model           | Accuracy   | Precision | Recall   | F1 Score |
|-----------------|------------|-----------|----------|----------|
| XBGClassifier   | 0.93       | 0.9350    | 0.9265   | 0.9282   |
| SVC             | 0.90       | 0.8526    | 0.8971   | 0.8736   |
| SVC (variant)   | 0.94       | 0.9480    | 0.9412   | 0.9363   |

The Random Forest model was also trained and evaluated, with metrics such as accuracy, precision, recall, and F1 score calculated and visualized. Confusion matrices and classification reports were plotted for deeper insight.

### Feature Importance

SHAP analysis was performed to interpret feature importance for the Random Forest model, providing insights into which CBC parameters most influence anemia classification.
# Anemia-CBC-Analysis