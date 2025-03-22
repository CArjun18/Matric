import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
from kneed import KneeLocator  

df = pd.read_csv("Mall_Customers.csv")

print(df.isnull().sum())
print(df.head())

label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])


data = df[['Annual Income (k$)', 'Spending Score (1-100)', 'Age', 'Gender']]

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)


inertia = []
k_range = range(1, 15)

for k in k_range:
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
    kmeans.fit(scaled_data)
    inertia.append(kmeans.inertia_)


kl = KneeLocator(k_range, inertia, curve="convex", direction="decreasing")
optimal_k = kl.elbow
print(f"Optimal K: {optimal_k}")


plt.figure(figsize=(8, 6))
plt.plot(k_range, inertia, marker='o', color='b', label="WCSS")
plt.axvline(optimal_k, color='r', linestyle='--', label=f"Optimal K={optimal_k}")
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.xticks(k_range)
plt.legend()
plt.show()


kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(scaled_data)

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', palette='viridis', data=df, s=100, alpha=0.7)

centers = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='X', label='Centroids')

plt.title('Mall Customer Segmentation')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

print(df.groupby('Cluster').mean())
