'use client';

import { useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';

export default function NPICalculator() {
	const [stack, setStack] = useState<(number | string)[]>([]);
	const [input, setInput] = useState('');
	const [result, setResult] = useState<number | null>(null);
	const [errorMessage, setErrorMessage] = useState<string | null>(null);

	const pushToStack = () => {
		if (input) {
			setStack((prevStack) => [...prevStack, parseFloat(input)]);
			setInput('');
		}
	};

	const addOperationToStack = (operation: string) => {
		if (stack.length < 1) {
			setErrorMessage('Please enter at least one number before selecting an operation.');
			return;
		}
		setStack((prevStack) => [...prevStack, operation]);
	};

	// Perform the calculation using the entire stack (numbers + operations)
	const submitCalculation = async () => {
		if (stack.length < 3) {
			setErrorMessage('Please enter a valid expression (at least two numbers and an operation).');
			return;
		}

		try {
			// Send the stack array directly as the body
			const response = await fetch('http://localhost:8001/calculate', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(stack)
			});

			if (!response.ok) {
				const error = await response.json();
				throw new Error(error.detail);
			}

			const data = await response.json();
			setResult(data.result);
			setErrorMessage(null);
		} catch (error) {
			console.error('Error performing operation:', error);
			setErrorMessage(`Something went wrong, please try again. Message: ${error}`);
		}
	};

	const getCSV = async () => {
		try {
			const response = await fetch('http://localhost:8001/export-csv');

			if (!response.ok) {
				const error = await response.json();
				throw new Error(error.detail);
			}

			const blob = await response.blob();

			const url = window.URL.createObjectURL(blob);
			const link = document.createElement('a');
			link.href = url;
			link.setAttribute('download', 'calculations.csv');
			document.body.appendChild(link);
			link.click();
			document.body.removeChild(link);
		} catch (error) {
			console.error('Error performing operation:', error);
			setErrorMessage(`Something went wrong, please try again. Message: ${error}`);
		}
	};

	return (
		<div className="flex h-screen w-screen flex-col items-center justify-center gap-8">
			<Card className="mx-auto w-full max-w-md">
				<CardHeader>
					<CardTitle>Calculatrice NPI</CardTitle>
				</CardHeader>
				<CardContent>
					<div className="flex flex-col items-center justify-center gap-4">
						<div className="min-h-[100px] w-full rounded-md bg-secondary p-2">
							<h3 className="mb-2 font-semibold">Stack:</h3>
							<div className="grid grid-cols-5 place-items-center px-4 py-2">
								{stack.map((item, index) => (
									<div key={index}>{item}</div>
								))}
							</div>
						</div>
						<div>
							<form
								onSubmit={(e) => {
									e.preventDefault();
									pushToStack();
								}}
								className="flex w-full gap-2"
							>
								<Input
									type="number"
									value={input}
									onChange={(e) => setInput(e.target.value)}
									placeholder="Enter a number"
								/>
								<Button onClick={pushToStack}>Push</Button>
							</form>
						</div>
						<h3 className="self-start font-semibold">Select Operation:</h3>
						<div className="grid w-full grid-cols-2 gap-2">
							<Button onClick={() => addOperationToStack('+')}>+</Button>
							<Button onClick={() => addOperationToStack('-')}>-</Button>
							<Button onClick={() => addOperationToStack('*')}>*</Button>
							<Button onClick={() => addOperationToStack('/')}>/</Button>
						</div>
						<Button className="mt-4 w-full" onClick={submitCalculation}>
							Calculer
						</Button>
						{result !== null && (
							<div className="mt-4">
								<h3 className="font-semibold">Result:</h3>
								<div className="text-2xl font-bold">{result}</div>
							</div>
						)}
						{errorMessage && <div className="text-red-600">{errorMessage}</div>}
					</div>
				</CardContent>
			</Card>

			<Button onClick={getCSV}>Télécharger les donnéeszb</Button>
		</div>
	);
}
