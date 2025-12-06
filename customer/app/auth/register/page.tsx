"use client"
import React, { useState } from "react"
import Link from "next/link"
import { motion } from "framer-motion"

const RegisterPage = () => {
  const [form, setForm] = useState({ fullName: "", username: "", email: "", password: "" })

  const handleChange = (e:any) => {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  const handleSubmit = (e:any) => {
    e.preventDefault()
    console.log(form)
  }

  return (
    <div className="min-h-screen flex items-center justify-center  p-4">
      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
        className="w-full max-w-md bg-white/70 backdrop-blur-xl shadow-xl rounded-2xl p-8 border border-white/40"
      >
        <h2 className="text-3xl font-bold text-center mb-6 text-gray-800">Create Account ✨</h2>
        <p className="text-center text-gray-600 mb-8">Join us and start your journey.</p>

        <form onSubmit={handleSubmit} className="space-y-5">

          {/* Full Name */}
          <div>
            <label className="text-gray-700 font-medium">Full Name</label>
            <input
              type="text"
              name="fullName"
              value={form.fullName}
              onChange={handleChange}
              placeholder="Enter your full name"
              className="w-full mt-1 px-4 py-2.5 rounded-xl border border-gray-300 focus:ring-2 focus:ring-purple-500 focus:outline-none shadow-sm bg-white/80"
            />
          </div>

          {/* Username */}
          <div>
            <label className="text-gray-700 font-medium">Username</label>
            <input
              type="text"
              name="username"
              value={form.username}
              onChange={handleChange}
              placeholder="Choose a username"
              className="w-full mt-1 px-4 py-2.5 rounded-xl border border-gray-300 focus:ring-2 focus:ring-purple-500 focus:outline-none shadow-sm bg-white/80"
            />
          </div>

          {/* Email */}
          <div>
            <label className="text-gray-700 font-medium">Email</label>
            <input
              type="email"
              name="email"
              value={form.email}
              onChange={handleChange}
              placeholder="Enter your email"
              className="w-full mt-1 px-4 py-2.5 rounded-xl border border-gray-300 focus:ring-2 focus:ring-purple-500 focus:outline-none shadow-sm bg-white/80"
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
              placeholder="Create a password"
              className="w-full mt-1 px-4 py-2.5 rounded-xl border border-gray-300 focus:ring-2 focus:ring-purple-500 focus:outline-none shadow-sm bg-white/80"
            />
          </div>

          {/* Submit */}
          <button
            type="submit"
            className="w-full py-2.5 bg-gradient-to-r from-purple-600 to-pink-600 text-white rounded-xl font-semibold shadow-md hover:opacity-90 hover:scale-[1.02] transition-all"
          >
            Register
          </button>
        </form>

        <p className="text-center text-gray-600 mt-6">
          Already have an account?{" "}
          <Link href="/auth/login" className="text-purple-600 font-semibold hover:underline">
            Login
          </Link>
        </p>
      </motion.div>
    </div>
  )
}

export default RegisterPage
