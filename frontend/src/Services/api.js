const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export async function predictCustomer(payload) {
  const response = await fetch(`${API_BASE_URL}/predict`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error("Prediction failed");
  }

  return response.json();
}
