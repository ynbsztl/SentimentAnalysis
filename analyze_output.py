import csv
from arguments import args
from analyzer import Analyzer

if __name__ == "__main__":

    print("Please wait while the analyzer is being initialized.")

    analyzer = Analyzer(will_train=False, args=args)

    input_file = "data/input.tsv"
    output_file = "data/output.tsv"

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile, delimiter='\t')
        writer = csv.writer(outfile, delimiter='\t')

        # Write header for output file
        writer.writerow(["Text", "Sentiment", "Probability"])

        for row in reader:
            text = row[0]
            sentiment, percentage = analyzer.classify_sentiment(text)
            writer.writerow([text, sentiment, percentage])

    print("Sentiment analysis completed. Results saved to output.tsv")

