import Link from 'next/link'
import React from 'react'

const Name = () => {
  return (
    <Link className='text-2xl font-semibold text-red-500 cursor-pointer hover:text-blue-500 duration-300 transition-all' href={"/"}>
        Buddies Hub
    </Link>
  )
}

export default Name