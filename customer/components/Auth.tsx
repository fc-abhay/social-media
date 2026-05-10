"use client";
import { fetchUserInfo, logout } from "@/store/auth/userStore";
import { useAppDispatch, useAppSelector } from "@/store/store";
import Link from "next/link";
import { useEffect, useState } from "react";

const Auth = () => {

    const [openMenu, setOpenMenu] = useState(false);
    const dispatch = useAppDispatch();
    const { user } = useAppSelector((state) => state.userInfo);

    // Fetch user ONCE when component mounts
    useEffect(() => {
        const token = localStorage.getItem("token");
        if (token) dispatch(fetchUserInfo());
    }, []);


    return (
        <div className="relative">
            {user!==null ? (
                <div className="flex items-center gap-3">
                    {/* AVATAR + NAME */}
                    <button
                        onClick={() => setOpenMenu(!openMenu)}
                        className="flex items-center gap-2 p-2 rounded-xl bg-gray-100 hover:bg-gray-200 cursor-pointer transition"
                    >
                        <img
                            src={`https://ui-avatars.com/api/?name=${user.username}&background=4f46e5&color=fff`}
                            alt="User"
                            className="w-10 h-10 rounded-full border border-gray-300"
                        />
                        <div className="flex flex-col text-left">
                            <span className="font-semibold">{user.username}</span>
                            <span className="text-xs text-gray-400">{user.email}</span>
                        </div>
                    </button>

                    {/* DROPDOWN MENU */}
                    {openMenu && (
                        <div className="absolute right-0 top-14 bg-white shadow-xl rounded-xl w-52 border border-gray-200 animate-fadeIn">
                            <ul className="flex flex-col py-2 px-4 gap-2">
                                <Link href="/dashboard" className="menu-item">Dashboard</Link>
                                <Link href="/profile" className="menu-item">Profile</Link>
                                <Link href="/settings" className="menu-item">Settings</Link>

                                <button
                                    onClick={() => dispatch(logout())}
                                    className="menu-item text-red-500 hover:bg-red-50"
                                >
                                    Logout
                                </button>
                            </ul>
                        </div>
                    )}
                </div>
            ) : (
                <div className="flex items-center gap-4">
                    <Link
                        href="/auth/login"
                        className="px-5 py-2 rounded-xl font-semibold bg-gradient-to-r from-indigo-500 to-blue-600 text-white shadow-lg hover:scale-105 transition"
                    >
                        Login
                    </Link>

                    <Link
                        href="/auth/register"
                        className="px-5 py-2 rounded-xl font-semibold bg-gradient-to-r from-indigo-500 to-blue-600 text-white shadow-lg hover:scale-105 transition"
                    >
                        Register
                    </Link>
                </div>
            )}
        </div>
    );
};

export default Auth;
