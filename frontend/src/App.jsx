import { useState } from "react";
import Header from "./components/Header";
import NumericFields from "./components/NumericFields";
import BinaryFields from "./components/BinaryFields";
import CategoricalFields from "./components/CategoricalFields";
import SubmitButton from "./components/SubmitButton";
import ResultCard from "./components/ResultCard";
import { predictCustomer } from "./Services/api";
import "./App.css";

export default function App() {
  const [formData, setFormData] = useState({
    age: 30,
    balance: 0,
    day: 1,
    duration: 0,
    campaign: 1,
    pdays: -1,
    previous: 0,
    default: 0,
    housing: 0,
    loan: 0,
    job: "management",
    marital: "married",
    education: "secondary",
    contact: "unknown",
    month: "may",
    poutcome: "unknown",
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const res = await predictCustomer(formData);
      setResult(res);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="container">
      <Header />

      <form onSubmit={handleSubmit}>
        <NumericField formData={formData} setFormData={setFormData} />
        <BinaryFields formData={formData} setFormData={setFormData} />
        <CategoricalFields formData={formData} setFormData={setFormData} />
        <SubmitButton loading={loading} />
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}
      <ResultCard result={result} />
    </div>
  );
}
