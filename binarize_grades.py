from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np


def binarize_grades(motion_data, grader_column, return_centers=False, use_centers=None):
    # scale the data to be able to calculate the euclidean distance
    scaler = StandardScaler()
    scaled_motion_data = scaler.fit_transform(motion_data)
    scaled_motion_data = pd.DataFrame(scaled_motion_data, columns=motion_data.columns, index=motion_data.index)
    
    # Define good (1, 2) and bad (4, 5) clusters
    idx_cluster_0 = grader_column.isin([1, 2])
    idx_cluster_1 = grader_column.isin([4, 5])

    # check how many rows are in each cluster
    print(f'Cluster 0: {idx_cluster_0.sum()}')
    print(f'Cluster 1: {idx_cluster_1.sum()}')
    print(f'Unassigned: {(grader_column == 3).sum()}')
    
    # Compute cluster centers for good and bad
    if use_centers:
        cluster_0_center, cluster_1_center = use_centers
    else:
        cluster_0_center = scaled_motion_data.loc[idx_cluster_0].mean()
        cluster_1_center = scaled_motion_data.loc[idx_cluster_1].mean()

    distances_to_0 = np.linalg.norm(scaled_motion_data.values - cluster_0_center.values, axis=1)
    distances_to_1 = np.linalg.norm(scaled_motion_data.values - cluster_1_center.values, axis=1)

    # Initialize a new cluster column (0 for good, 1 for bad)
    cluster_assignment = np.where(idx_cluster_0, 0, np.where(idx_cluster_1, 1, -1))  # -1 for unassigned (grade 3)
 
    # Assign grade 3 rows based on proximity to good/bad clusters
    unassigned_idx = grader_column == 3
    cluster_assignment[unassigned_idx] = np.where(
        distances_to_0[unassigned_idx] < distances_to_1[unassigned_idx], 0, 1
    )
   
    motion_data['cluster'] = cluster_assignment
    if return_centers:
        return motion_data, cluster_0_center, cluster_1_center
    
    return motion_data

