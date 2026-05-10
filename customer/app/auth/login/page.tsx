"use client"
import React, { useState } from "react"
import Link from "next/link"
import { motion } from "framer-motion"
import axiosClient from "@/utils/axiosClient"
import { toast } from "react-toastify"
import { useRouter } from "next/navigation"
import { useAppSelector } from "@/store/store"


const LoginPage = () => {
  const [form, setForm] = useState({ username: "", password: "" })
  const router=useRouter();
  const [loading,setLoading]=useState<boolean>(false)

  const handleChange = (e:any) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = async(e:any) => {
    setLoading(true)
    e.preventDefault()
    const {data,status} =await axiosClient.post("/auth/login/",form);
    if(status===200){
      toast.success(data.message)
      localStorage.setItem("token",data.token)
      router.replace("/")
    }else{
      toast.error(data.message)
    }
    setLoading(false)
  }

  return (
    <div className="min-h-screen flex items-center justify-center  p-4">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
        className="w-full max-w-md bg-white/70 backdrop-blur-xl shadow-xl rounded-2xl p-8 border border-white/40"
      >
        <h2 className="text-3xl font-bold text-center mb-6 text-gray-800">Welcome Back 👋</h2>
        <p className="text-center text-gray-600 mb-8">Login to continue exploring.</p>

        <form onSubmit={handleSubmit} className="space-y-5">
          {/* Username */}
          <div>
            <label className="text-gray-700 font-medium">Username</label>
            <input
              type="text"
              name="username"
              value={form.username}
              onChange={handleChange}
              placeholder="Enter your username"
              className="w-full mt-1 px-4 py-2.5 rounded-xl border border-gray-300 focus:ring-2 focus:ring-indigo-500 focus:outline-none shadow-sm bg-white/80"
            />
          </div>

          {/* Password */}
          <div>
            <label className="text-gray-700 font-medium">Password</label>
            <input
              type="password"
              name="password"
              value={form.password}
              onChange={handleChange}
              placeholder="Enter your password"
              className="w-full mt-1 px-4 py-2.5 rounded-xl border border-gray-300 focus:ring-2 focus:ring-indigo-500 focus:outline-none shadow-sm bg-white/80"
            />
          </div>

          {/* Submit */}
          <button
            type="submit"
            disabled={loading}
            className="w-full cursor-pointer py-2.5 bg-gradient-to-r from-indigo-600 to-blue-600 text-white rounded-xl font-semibold shadow-md hover:opacity-90 hover:scale-[1.02] transition-all"
          >
            {
              loading ? "Logging in..." : "Login"
            }
          </button>
        </form>

        {/* Bottom */}
        <p className="text-center text-gray-600 mt-6">
          Don't have an account?{" "}
          <Link href="/auth/register" className="text-indigo-600 font-semibold hover:underline">
            Register
          </Link>
        </p>
      </motion.div>
    </div>
  )
}

export default LoginPage
