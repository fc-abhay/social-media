import Link from 'next/link'
import React from 'react'

const NotFound = () => {
  return (
    <section className="bg-white flex items-center justify-center min-h-screen dark:bg-gray-900">
      <div className="px-4 mx-auto max-w-screen-xl py-8 lg:py-16">
        <div className="mx-auto max-w-screen-sm text-center">
          
          <h1 className="mb-4 text-7xl tracking-tight font-extrabold lg:text-9xl text-blue-600 dark:text-blue-500">
            404
          </h1>

          <p className="mb-4 text-3xl tracking-tight font-bold text-gray-900 md:text-4xl dark:text-white">
            Something's missing.
          </p>

          <p className="mb-6 text-lg font-light text-gray-500 dark:text-gray-400">
            Sorry, we can't find that page. You can explore more on the homepage.
          </p>

          <Link
            href="/"
            className="inline-flex text-white bg-blue-600 hover:bg-blue-700 focus:ring-4 
            focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 dark:bg-blue-500 
            dark:hover:bg-blue-600 dark:focus:ring-blue-900 transition"
          >
            Back to Homepage
          </Link>

        </div>
      </div>
    </section>
  )
}

export default NotFound
