import React from 'react'

const Address = ({data}) => {

  if (!data.transactions) return <p className='font-bold'>Address not found</p>

  const options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };


  return (
    <div>

      <p className='text-2xl font-bold'>Balance: {data.balance}</p>

      {data.transactions.map((transaction, index) => (
        (
          <div key={index} className='mb-2'>
            <p><span className='font-bold text-lg'>Transaction  </span><span className='text-sky-600 font-bold'>#{transaction.transaction_id}</span></p>
            <p className='text-gray-500 ms-2'>@{new Date(transaction.timestamp * 1000).toLocaleString(undefined, options)}</p>
            <p className='ms-2'>Sender: {transaction.sender}</p>
            <p className='ms-2'>Recipient: {transaction.recipient}</p>
            <p className='ms-2'>Amount: {transaction.amount}</p>
          </div>

        )
      ))}

    </div>
  )
}

export default Address