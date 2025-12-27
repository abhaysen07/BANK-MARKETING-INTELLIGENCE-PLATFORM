// src/components/SubmitButton.jsx

export default function SubmitButton({ loading }) {
  return (
    <button disabled={loading}>
      {loading ? "Predicting..." : "Predict"}
    </button>
  );
}