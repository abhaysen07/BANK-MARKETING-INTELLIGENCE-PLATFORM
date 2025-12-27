// src/components/ResultCard.jsx

export default function ResultCard({ result }) {
  if (!result) return null;

  return (
    <div style={{ marginTop: "20px", padding: "15px", border: "1px solid #444" }}>
      <h3>Prediction Result</h3>
      <p><strong>Prediction:</strong> {result.prediction}</p>
      <p><strong>Probability:</strong> {result.probability}</p>
      <p><strong>Confidence:</strong> {result.confidence}</p>
      <p><strong>Recommendation:</strong> {result.recommendation}</p>
    </div>
  );
}
