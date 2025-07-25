# real-estate-ml
Real estate pricing model with ML, geostatic and hedonic analysis 

# Real Estate ML Model

This project models and predicts real estate prices using machine learning and hedonic pricing theory.

## Project Goals
- Predict housing prices from real data
- Create a hedonic price index
- Simulate investment strategies
- Deploy an interactive dashboard

## Current Progress
- [x] Project setup
- [x] EDA started
- [x] Feature engineering
- [x] Modeling (Lasso Regression Complete)
- [ ] Streamlit app

## Modeling Summary
- **Model**: Lasso Regression (with cross-validation for alpha selection)
- **Test R²**: 0.9648
- **Test MSE**: 0.0189

### Most Important Features
| Feature             | Coefficient |
|---------------------|-------------|
| Index               | 0.8781      |
| TerracedIndex       | -0.6356     |
| FlatIndex           | 0.2918      |
| Cash1m%Change       | -0.1448     |
| Terraced12m%Change  | 0.1103      |

## Folder Structure
- `app/`: Streamlit app (to be developed)
- `data/`: Raw and cleaned datasets
- `models/`: Trained models and serialized outputs
- `notebooks/`: Jupyter notebooks for EDA and modeling
- `simulations/`: Investment simulations and backtesting
- `src/`: Source code and utilities

## Next Steps
- Begin geospatial + index analysis (Phase 1, Day 3)
- Build hedonic price index
- Design and test investment strategies
- Integrate modeling into interactive Streamlit app