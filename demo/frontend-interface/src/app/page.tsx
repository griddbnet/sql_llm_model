'use client'; //required for use with react hook form for some reason
import * as React from "react";
import { useForm, SubmitHandler } from "react-hook-form";

type Question = {
  question: string
  context: string
}

const URL = 'http://localhost:5000/query';

export default function Home() {

  const [formedQuery, setFormedQuery] = React.useState("Please Submit Question & Context");

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<Question>()

  const onSubmit: SubmitHandler<Question> = (data: Question) => {
    console.log(data);
    fetch(URL, {
      method: "POST",
      mode: "cors",
      cache: "no-cache",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .then(res => res.text())
      .then(
        result => {
          setFormedQuery(result);
        })
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-start p-24">
      <div className="flex-col z-10 w-full max-w-5xl items-center lg:flex">
        <h1 className="text-neutral-200 my-5 text-xl"> Ask A Question </h1>
        <form onSubmit={handleSubmit(onSubmit)}>
          <section className="flex flex-col justify-center align-center gap-4">
            <textarea className="text-stone-950 p-2" defaultValue="Question" {...register("question", { required: true })} />
            <textarea className="text-stone-950 p-2" defaultValue="Context" {...register("context", { required: true })} />
            {errors.question && <span>This field is required</span>}
            {errors.context && <span>This field is required</span>}
          </section>
          <section className="flex justify-center">
            <input className="bg-slate-600 p-2 my-4 rounded-md" type="submit" />
          </section>
        </form>

      <p className="text-blue-300 my-6 text-4xl underline underline-offset-8 font-semibold"> {formedQuery} </p>
      </div>
    </main>
  );
}