import axios from "axios";

const axiosClient = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || "https://social-media-wggv.onrender.com/v1/api",
  headers: {
    "Content-Type": "application/json",
  },
});

// ---- REQUEST INTERCEPTOR ----
axiosClient.interceptors.request.use(
  (config) => {
    if (typeof window !== "undefined") {
      const token = localStorage.getItem("auth_token");

      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// ---- RESPONSE INTERCEPTOR ----
axiosClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response && error.response.status === 401) {
      console.warn("⚠️ Unauthorized — clearing token");
      if (typeof window !== "undefined") {
        localStorage.removeItem("auth_token");
      }
    }

    return Promise.reject(error);
  }
);

export default axiosClient;
