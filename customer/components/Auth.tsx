"use client";
import Link from "next/link";
import React, { useState } from "react";

const Auth = () => {
    const [isLoggedIn, setIsLoggedIn] = useState<boolean>(true); // for testing
    const [openMenu, setOpenMenu] = useState<boolean>(false);

    const user = {
        name: "Abhay Gupta",
        avatar: "https://ui-avatars.com/api/?name=Abhay+Gupta&background=4f46e5&color=fff"
    };

    return (
        <div className="relative">

            {/* IF LOGGED IN */}
            {isLoggedIn ? (
                <div className="flex items-center gap-3">
                    {/* AVATAR + NAME */}
                    <button
                        onClick={() => setOpenMenu(!openMenu)}
                        className="flex items-center gap-2 p-2 rounded-xl hover:bg-gray-100 dark:hover:bg-gray-800 cursor-pointer transition"
                    >
                        <img
                            src={user.avatar}
                            alt="User"
                            className="w-10 h-10 rounded-full border border-gray-300"
                        />
                        <span className="font-semibold">{user.name}</span>
                    </button>

                    {/* DROPDOWN MENU */}
                    {openMenu && (
                        <div className="absolute right-0 top-14 bg-white dark:bg-gray-900 shadow-xl rounded-xl w-52 border border-gray-200 dark:border-gray-700 animate-fadeIn">
                            <ul className="flex flex-col py-2 px-4 gap-2">
                                <Link href="/dashboard" className="menu-item">
                                    Dashboard
                                </Link>
                                <Link href="/profile" className="menu-item">
                                    Profile
                                </Link>
                                <Link href="/settings" className="menu-item">
                                    Settings
                                </Link>

                                <button
                                    onClick={() => console.log("Logout")}
                                    className="menu-item cursor-pointer text-red-500 hover:bg-red-50"
                                >
                                    Logout
                                </button>
                            </ul>
                        </div>
                    )}
                </div>
            ) : (
                /* NOT LOGGED IN */
                <div className="flex items-center justify-between gap-4">
                    <Link
                        href="/auth/login"
                        className="px-5 py-2 rounded-xl font-semibold backdrop-blur-lg bg-gradient-to-r from-indigo-500 to-blue-600 text-white shadow-lg hover:opacity-90 hover:scale-105 transition-all duration-300"
                    >
                        Login
                    </Link>

                    <Link
                        href="/auth/register"
                        className="px-5 py-2 rounded-xl font-semibold backdrop-blur-lg bg-gradient-to-r from-indigo-500 to-blue-600 text-white shadow-lg hover:opacity-90 hover:scale-105 transition-all duration-300"
                    >
                        Register
                    </Link>
                </div>
            )}
        </div>
    );
};

export default Auth;
