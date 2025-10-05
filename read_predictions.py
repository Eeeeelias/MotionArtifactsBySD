import pandas as pd
import numpy as np


def get_all_predictions():
    tibia_old_patient = pd.read_csv(f'predictions/patient_set_tibia_old_predictions.csv')
    tibia_new_patient = pd.read_csv(f'predictions/patient_set_tibia_new_predictions.csv')
    radius_old_patient = pd.read_csv(f'predictions/patient_set_radius_old_predictions.csv')
    radius_new_patient = pd.read_csv(f'predictions/patient_set_radius_new_predictions.csv')

    tibia_old_balanced_patient = pd.read_csv(f'predictions/patient_set_tibia_old_balanced_predictions.csv')
    tibia_new_balanced_patient = pd.read_csv(f'predictions/patient_set_tibia_new_balanced_predictions.csv')
    radius_old_balanced_patient = pd.read_csv(f'predictions/patient_set_radius_old_balanced_predictions.csv')
    radius_new_balanced_patient = pd.read_csv(f'predictions/patient_set_radius_new_balanced_predictions.csv')

    tibia_old = pd.read_csv(f'predictions/tibia_old_predictions.csv')
    tibia_new = pd.read_csv(f'predictions/tibia_new_predictions.csv')
    radius_old = pd.read_csv(f'predictions/radius_old_predictions.csv')
    radius_new = pd.read_csv(f'predictions/radius_new_predictions.csv')

    tibia_old_balanced = pd.read_csv(f'predictions/tibia_old_balanced_predictions.csv')
    tibia_new_balanced = pd.read_csv(f'predictions/tibia_new_balanced_predictions.csv')
    radius_old_balanced = pd.read_csv(f'predictions/radius_old_balanced_predictions.csv')
    radius_new_balanced = pd.read_csv(f'predictions/radius_new_balanced_predictions.csv')

    # concat all predictions and add column for model
    tibia_old['model'] = 'Tibia XCT1'
    tibia_old_balanced['model'] = 'Tibia XCT1'
    tibia_old_patient['model'] = 'Tibia XCT1'
    tibia_old_balanced_patient['model'] = 'Tibia XCT1'

    tibia_new['model'] = 'Tibia XCT2'
    tibia_new_balanced['model'] = 'Tibia XCT2'
    tibia_new_patient['model'] = 'Tibia XCT2'
    tibia_new_balanced_patient['model'] = 'Tibia XCT2'

    radius_old['model'] = 'Radius XCT1'
    radius_old_balanced['model'] = 'Radius XCT1'
    radius_old_patient['model'] = 'Radius XCT1'
    radius_old_balanced_patient['model'] = 'Radius XCT1'

    radius_new['model'] = 'Radius XCT2'
    radius_new_balanced['model'] = 'Radius XCT2'
    radius_new_patient['model'] = 'Radius XCT2'
    radius_new_balanced_patient['model'] = 'Radius XCT2'

    normal_predictions = pd.concat([tibia_old, tibia_new, radius_old, radius_new], ignore_index=True)
    balanced_predictions = pd.concat([tibia_old_balanced, tibia_new_balanced, radius_old_balanced, radius_new_balanced], ignore_index=True)
    normal_predictions_patient = pd.concat([tibia_old_patient, tibia_new_patient, radius_old_patient, radius_new_patient], ignore_index=True)
    balanced_predictions_patient = pd.concat([tibia_old_balanced_patient, tibia_new_balanced_patient, radius_old_balanced_patient, radius_new_balanced_patient], ignore_index=True)

    normal_predictions['no_pred'] = np.arange(len(normal_predictions))
    balanced_predictions['no_pred'] = np.arange(len(balanced_predictions))
    normal_predictions_patient['no_pred'] = np.arange(len(normal_predictions_patient))
    balanced_predictions_patient['no_pred'] = np.arange(len(balanced_predictions_patient)) 

    normal_predictions['balanced'] = False
    balanced_predictions['balanced'] = True
    normal_predictions_patient['balanced'] = False
    balanced_predictions_patient['balanced'] = True

    normal_predictions['samples'] = 'all'
    balanced_predictions['samples'] = 'all'
    normal_predictions_patient['samples'] = 'patients'
    balanced_predictions_patient['samples'] = 'patients'

    all_predictions = pd.concat([normal_predictions, balanced_predictions, 
                                normal_predictions_patient, balanced_predictions_patient], ignore_index=True)
    return all_predictions