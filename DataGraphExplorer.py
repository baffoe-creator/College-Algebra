import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
from io import StringIO

class DataGraphExplorer:
    def __init__(self):
        self.df = None
        self.column_names = []

    def load_csv(self):
        load_type = int(input("Choose load method:\n1. Upload from local (not supported in headless)\n2. Enter URL\n3. Use URL in code\nEnter choice (2 or 3): "))
        if load_type in [2, 3]:
            try:
                if load_type == 2:
                    url = input("Enter CSV URL:")
                    if url:
                        self._read_csv(url)
                elif load_type == 3:
                    default_url = "https://raw.githubusercontent.com/plotly/datasets/master/iris.csv"
                    self._read_csv(default_url)

                if self.df is not None:
                    print("Data loaded successfully!")
                    print("Headings:")
                    print(self.df.columns.tolist())
                    print("\nFirst two rows:")
                    print(self.df.head(2))
                    self.column_names = self.df.columns.tolist()
                    self.generate_graph()
            except Exception as e:
                print(f"Error loading data: {e}")

    def _read_csv(self, source):
        try:
            if source.startswith('http'):
                response = requests.get(source)
                response.raise_for_status()
                csv_data = StringIO(response.text)
                self.df = pd.read_csv(csv_data)
            else:
                raise ValueError("Local file upload not supported in headless mode.")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching URL: {e}")
        except ValueError as e:
            raise e
        except pd.errors.EmptyDataError:
            raise Exception("The CSV file is empty.")
        except pd.errors.ParserError:
            raise Exception("Error parsing the CSV file.")

    def generate_graph(self):
        if self.df is None or not self.column_names:
            print("No data loaded yet.")
            return

        col1 = input(f"Enter the name of the first column to plot:\nAvailable columns: {', '.join(self.column_names)}\n")
        if col1 and col1 in self.column_names:
            col2 = input(f"Enter the name of the second column to plot (leave blank for single variable):\nAvailable columns: {', '.join(self.column_names)}\n")
            if col2 == "":
                self._plot_single_variable(col1)
            elif col2 in self.column_names:
                plot_type = int(input("Choose plot type:\n1. Scatter Plot\n2. Line Graph\nEnter choice (1 or 2): "))
                if plot_type == 1:
                    self._plot_two_variables(col1, col2, 'scatter')
                elif plot_type == 2:
                    self._plot_two_variables(col1, col2, 'line')
                else:
                    print("Invalid plot type.")
            else:
                print(f"Column '{col2}' not found.")
        else:
            print(f"Column '{col1}' not found.")

    def _plot_single_variable(self, column):
        try:
            data = self.df[column].to_numpy()
            plt.figure(figsize=(8, 6))
            plt.hist(data, bins=10, edgecolor='black')
            plt.title(f'Distribution of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            plt.grid(True)
            plt.savefig(f'histogram_{column}.png') # Save the plot
            print(f"Histogram saved as histogram_{column}.png")
        except KeyError:
            print(f"Column '{column}' not found.")
        except Exception as e:
            print(f"An error occurred during plotting: {e}")

    def _plot_two_variables(self, col1, col2, plot_type='scatter'):
        try:
            x_data = self.df[col1].to_numpy()
            y_data = self.df[col2].to_numpy()
            plt.figure(figsize=(8, 6))
            if plot_type == 'scatter':
                plt.scatter(x_data, y_data)
                plt.title(f'Scatter Plot of {col1} vs {col2}')
                plt.xlabel(col1)
                plt.ylabel(col2)
                plt.savefig(f'scatter_{col1}_vs_{col2}.png') # Save the plot
                print(f"Scatter plot saved as scatter_{col1}_vs_{col2}.png")
            elif plot_type == 'line':
                plt.plot(x_data, y_data)
                plt.title(f'Line Graph of {col1} vs {col2}')
                plt.xlabel(col1)
                plt.ylabel(col2)
                plt.savefig(f'line_{col1}_vs_{col2}.png') # Save the plot
                print(f"Line graph saved as line_{col1}_vs_{col2}.png")
            plt.grid(True)
        except KeyError:
            print("One or both columns not found.")
        except Exception as e:
            print(f"An error occurred during plotting: {e}")

    def run(self):
        self.load_csv()

if __name__ == "__main__":
    explorer = DataGraphExplorer()
    explorer.run()
