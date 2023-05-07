import React from 'react'

const Transaction = ({data}) => {

  if (!data.transaction) return <p className='font-bold'>Transaction not found</p>

  const transaction = data.transaction
  const options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };


  return (
    <div>

      <div className='flex justify-between items-center'>
          <p className='font-bold'><span className='text-3xl'>Transaction</span></p>
          <p className='text-gray-500 hover:text-gray-900 transition duration-100 ease-in'>@{ new Date(transaction.timestamp * 1000).toLocaleString(undefined, options) }</p>
      </div>
      <p className='text-sky-600 font-bold mb-3'>#{transaction.transaction_id}</p>

      <div className='flex justify-between items-center mb-2 border-b'>
            <p className='text-lg'>Sender: </p>
            <p className='text-lg text-sky-600'>{transaction.sender}</p>
      </div>

      <div className='flex justify-between items-center mb-2 border-b'>
            <p className='text-lg'>Recipient: </p>
            <p className='text-lg text-sky-600'>{transaction.recipient}</p>
      </div>

      <div className='flex justify-between items-center mb-2 border-b'>
            <p className='text-lg'>Amount: </p>
            <p className='text-lg text-sky-600'>{transaction.amount}</p>
      </div>

    </div>

  )
}

export default Transaction