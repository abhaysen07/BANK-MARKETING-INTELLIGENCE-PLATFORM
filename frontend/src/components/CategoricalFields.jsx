// src/components/CategoricalFields.jsx

export default function CategoricalFields({ formData, setFormData }) {
  const options = {
    job: [
      "admin.",
      "blue-collar",
      "entrepreneur",
      "housemaid",
      "management",
      "retired",
      "self-employed",
      "services",
      "student",
      "technician",
      "unemployed",
      "unknown",
    ],
    marital: ["married", "single", "divorced"],
    education: ["primary", "secondary", "tertiary", "unknown"],
    contact: ["cellular", "telephone", "unknown"],
    month: [
      "jan","feb","mar","apr","may","jun",
      "jul","aug","sep","oct","nov","dec",
    ],
    poutcome: ["failure", "other", "success", "unknown"],
  };

  return (
    <fieldset>
      <legend>Categorical Details</legend>

      {Object.entries(options).map(([field, values]) => (
        <div key={field}>
          <label>{field}</label>
          <select
            value={formData[field]}
            onChange={(e) =>
              setFormData({ ...formData, [field]: e.target.value })
            }
          >
            {values.map((v) => (
              <option key={v} value={v}>
                {v}
              </option>
            ))}
          </select>
        </div>
      ))}
    </fieldset>
  );
}
