// src/components/NumericFields.jsx

export default function NumericFields({ formData, setFormData }) {
  const fields = [
    "age",
    "balance",
    "day",
    "duration",
    "campaign",
    "pdays",
    "previous",
  ];

  return (
    <fieldset>
      <legend>Numeric Details</legend>

      {fields.map((field) => (
        <div key={field}>
          <label>{field}</label>
          <input
            type="number"
            value={formData[field]}
            onChange={(e) =>
              setFormData({ ...formData, [field]: Number(e.target.value) })
            }
          />
        </div>
      ))}
    </fieldset>
  );
}