// src/components/BinaryFields.jsx

export default function BinaryFields({ formData, setFormData }) {
  const fields = ["default", "housing", "loan"];

  return (
    <fieldset>
      <legend>Binary Options</legend>

      {fields.map((field) => (
        <div key={field}>
          <label>{field}</label>
          <select
            value={formData[field]}
            onChange={(e) =>
              setFormData({ ...formData, [field]: Number(e.target.value) })
            }
          >
            <option value={0}>No</option>
            <option value={1}>Yes</option>
          </select>
        </div>
      ))}
    </fieldset>
  );
}