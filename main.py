# Import libraries
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml

data = fetch_openml(name='wine', version=1, as_frame=True)

df = data.frame
features = df.columns
selected_features = (features[1], features[2] , features[5], features[10])

reference_feature = selected_features[0]  # The reference feature
comparison_feature = selected_features[3]  # A feature to compare to

# Create a scatter plot for the selected pair
plt.figure(figsize=(8, 6))
plt.scatter(df[reference_feature], df[comparison_feature], alpha=0.6 , c= 'green')
plt.xlabel(reference_feature , fontsize = 20)
plt.ylabel(comparison_feature , fontsize = 20)

# Save the plot as an image file
plt.savefig('correlation_plot.png')

plt.show()
