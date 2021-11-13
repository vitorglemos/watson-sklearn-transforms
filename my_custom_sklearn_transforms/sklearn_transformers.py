from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        loan_purpose_map = {'CAR_USED': 1, 'CAR_NEW': 2,
                            'APPLIANCES': 3, 'FURNITURE': 4,
                            'VACATION': 5, 'RADIO_TV': 6,
                            'OTHER': 7, 'REPAIRS': 8, 'RETRAINING': 9,
                            'EDUCATION': 10, 'BUSINESS': 11}

        other_loan_map = {'NONE': 0, 'CO-APPLICANT': 1, 'GUARANTOR': 2}
        installment_map = {'NONE': 0, 'STORES': 1, 'BANK': 2}

        credit_history_map = {'ALL_CREDITS_PAID_BACK': 1, 'CREDITS_PAID_TO_DATE': 2, 'PRIOR_PAYMENTS_DELAYED': 3,
                              'OUTSTANDING_CREDIT': 4, 'NO_CREDITS': 5}

        data["CREDIT_HISTORY"] = data["CREDIT_HISTORY"].replace(credit_history_map)
        data["CHECKING_BALANCE"] = data["CHECKING_BALANCE"].replace({"NO_CHECKING": 0})
        data["EXISTING_SAVINGS"] = data["EXISTING_SAVINGS"].replace({"UNKNOWN": 0})

        data["LOAN_PURPOSE"] = data["LOAN_PURPOSE"].replace(loan_purpose_map)
        data["OTHERS_ON_LOAN"] = data["OTHERS_ON_LOAN"].replace(other_loan_map)
        data["INSTALLMENT_PLANS"] = data["INSTALLMENT_PLANS"].replace(installment_map)

        sex_map = {'F': 0, 'M': 1}
        property_map = {'UNKNOWN': 0, 'SAVINGS_INSURANCE': 1, 'REAL_ESTATE': 2, 'CAR_OTHER': 3}
        housing_map = {'OWN': 1, 'RENT': 2, 'FREE': 3}

        data["SEX"] = data["SEX"].replace(sex_map)
        data["PROPERTY"] = data["PROPERTY"].replace(property_map)
        data["HOUSING"] = data["HOUSING"].replace(housing_map)
        
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
