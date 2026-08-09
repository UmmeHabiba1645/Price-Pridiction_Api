import axios from "axios";

const API = axios.create({
  baseURL: "https://price-pridictionapi-production.up.railway.app",
  headers: {
    "Content-Type": "application/json",
  },
});

export const predictPrice = async (data) => {
  try {
    const response = await API.post("/predict", data);
    return response.data;
  } catch (error) {
    console.error("Prediction API Error:", error);

    if (error.response) {
      throw new Error(
        error.response.data?.error || "Prediction failed"
      );
    }

    throw new Error("Unable to connect to prediction server");
  }
};

export default API;