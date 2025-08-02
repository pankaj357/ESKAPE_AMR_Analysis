import pandas as pd
from glob import glob
import os

def main():
    try:
        # Get all result files
        amr_files = glob("AMRF_output/*_amrfinder.txt")
        
        if not amr_files:
            raise FileNotFoundError("No AMR result files found in AMRF_output/")
        
        # Process files
        data = []
        for file in amr_files:
            strain = os.path.basename(file).replace('_amrfinder.txt', '')
            with open(file) as f:
                for line in f:
                    if not line.startswith('#') and line.strip():
                        parts = line.strip().split('\t')
                        if len(parts) >= 6:
                            data.append({
                                'Gene': parts[1],
                                'Strain': strain,
                                'Subtype': parts[5]
                            })
        
        if not data:
            raise ValueError("No valid AMR data found in the files")
        
        # Create and save outputs
        df = pd.DataFrame(data)
        df.to_csv("amr_full_results.csv", index=False)
        
        # Create presence/absence matrix
        matrix = df.pivot_table(
            index='Gene',
            columns='Strain',
            values='Subtype',
            aggfunc=lambda x: 1,
            fill_value=0
        )
        matrix.to_csv("amr_matrix.csv")
        
        print("Successfully created:")
        print(f"- {len(df)} AMR records in amr_full_results.csv")
        print(f"- Matrix with {matrix.shape[0]} genes across {matrix.shape[1]} strains in amr_matrix.csv")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Please check:")
        print("1. AMRF_output/ contains *_amrfinder.txt files")
        print("2. The files have at least 6 tab-separated columns")
        print("3. You have write permissions in this directory")

if __name__ == "__main__":
    main()