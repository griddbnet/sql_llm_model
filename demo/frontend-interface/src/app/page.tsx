'use client'; //required for use with react hook form for some reason
import * as React from "react";
import { useForm, SubmitHandler } from "react-hook-form";
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { MagnifyingGlass } from 'react-loader-spinner'

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
  },
});

import MaterialTable from "./_components/MaterialTable"

type Question = {
  question: string
}

const URL = '/nlquery';
//const resURL = '/nlquery'

const initialQuestion = "What is the highest bytesSent for server baz?";
const initialQuery = "SELECT MAX(value) FROM event_bar WHERE event_id = 10 and time_fired > TIMESTAMP('2016-04-01T00:00:00Z') and time_fired < TIMESTAMP('2016-05-01T00:00:00Z')";

const examples = [
  {
    num: 1,
    question: "What is the highest bytesSent for server baz?",
    context: "CREATE TABLE head (name VARCHAR, born_state VARCHAR, age VARCHAR)"
  },
  {
    num: 2,
    context: "CREATE TABLE IF NOT EXISTS devices (device_id INTEGER, ts TIMESTAMP, co DOUBLE, humidity DOUBLE,light BOOL,lpg DOUBLE,motion BOOL,smoke DOUBLE,temp DOUBLE);",
    question: "What is the average contentLength in March 9, 2009 for the server foo?",
  },
  {
    num: 3,
    context: "CREATE TABLE IF NOT EXISTS iot_meter_foo (meter_id INTEGER, ts TIMESTAMP, kwh DOUBLE, temp DOUBLE, aqi DOUBLE); CREATE TABLE IF NOT EXISTS iot_meter_bar (meter_id INTEGER, ts TIMESTAMP, kwh DOUBLE, temp DOUBLE, aqi DOUBLE); CREATE TABLE IF NOT EXISTS iot_meter_baz (meter_id INTEGER, ts TIMESTAMP, kwh DOUBLE, temp DOUBLE, aqi DOUBLE);",
    question: "How many status code 404 on server bar on April 4, 2010?",
  }

];

export default function Home() {

  const [formedQuery, setFormedQuery] = React.useState("");
  const [toggleExamples, setToggleExamples] = React.useState(false);
  const [queryResults, setQueryResults] = React.useState([]);
  const [modelTime, setModelTime] = React.useState(0);
  const [queryTime, setQueryTime] = React.useState(0);
  const [loading, setLoading] = React.useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<Question>()

  const onSubmit: SubmitHandler<Question> = (data: Question) => {
    console.log(data);
    setLoading(true);
    fetch(`${URL}?question=${data.question}`, {
      method: "GET",
      mode: "no-cors",
      cache: "no-cache"
    })
      .then(res => res.json())
      .then(
        result => {
          setFormedQuery(result.query);
          setModelTime(result.model_time)
          setQueryTime(result.query_time)
          setQueryResults(result.results);
          console.log(result)
          setLoading(false);
        })
  }

  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <button
        className="p-2 absolute left-0 top-24 bg-gray-400 rounded-r-lg  bg-gray-300 cursor-pointer text-align-center"
        style={{ display: toggleExamples ? "none" : "block" }}
        onClick={() => setToggleExamples(!toggleExamples)}
      >
        <span className="text-slate-900"> Show </span><br />  <span className="text-slate-900"> Examples</span>
      </button>


      <div
        className="absolute left-0 top-24 bg-gray-400 max-w-96 rounded-sm z-20"
        style={{ display: toggleExamples ? "block" : "none" }}
      >
        <div className="m-5">
          <button
            className="absolute top-0 right-0 m-1 px-2 py-1 border border-gray-600 cursor-pointer bg-gray-500"
            onClick={() => setToggleExamples(!toggleExamples)}
          >
            X
          </button>
          <span className="text-2xl text-slate-900"> Examples </span>
          <ol className="text-md text-slate-800">
            {
              examples.map(example => (
                <div className="mx-2 my-6 border border-dotted" key={example.num}>
                  <li className="m-2">
                    <span className="underline">question:</span>  <span className="font-semibold"> {example.question} </span>
                  </li>
                </div>

              ))
            }
          </ol>
        </div>
      </div>


      <main className="flex min-h-screen flex-col items-center justify-start p-24">
        <div
          className="flex w-full max-w-5xl items-center lg:flex justify-around"
          style={{
            opacity: loading ? "0.5" : "1"
          }}
        >
          <div className="flex-col">
            <h1 className="text-neutral-200 my-5 text-xl justify-center"> Ask A Question </h1>
            <form onSubmit={handleSubmit(onSubmit)}>
              <section className="flex flex-col justify-center align-center gap-4">
                <textarea className="text-stone-950 p-2 w-80 h-20" defaultValue={initialQuestion} {...register("question", { required: true })} />
                {errors.question && <span>This field is required</span>}
              </section>
              <section className="flex justify-center">
                <input className="bg-slate-600 px-3 py-2 my-4 rounded-md cursor-pointer" type="submit" />
              </section>
            </form>
          </div>

          <div className="flex-col">
            <h3 className="text-neutral-200 my-5 text-xl justify-center"> Generated SQL Query</h3>

            <div className="bg-stone-900 rounded-md p-6  border border-slate-600 shadow-lg shadow-indigo-500/40 my-5 min-w-96 hover:z-50 ">
              <pre className="text-blue-300 my-6 text-xl font-semibold leading-8 max-h-64 max-w-2xl overflow-auto whitespace-pre-wrap "> {formedQuery} </pre>
            </div>
          </div>
        </div>

        <div className="flex-col w-full my-5 max-w-5xl lg:flex item-center">

          {
            loading
              ?
              <MagnifyingGlass
                visible={true}
                height="300"
                width="300"
                ariaLabel="magnifying-glass-loading"
                wrapperStyle={{}}
                wrapperClass="magnifying-glass-wrapper"
                glassColor="#c0efff"
                color="#e15b64"
              />
              :
              <></>
          }

          {queryResults.length > 0
            ?
            <MaterialTable
              queryResults={queryResults}
              modelTime={modelTime}
              queryTime={queryTime}
            />
            :
            <></>
          }
        </div>

      </main>

    </ThemeProvider>
  );
}
