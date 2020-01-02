module ErrorHandling
open System
open System

let handleErrorByThrowingException() = failwith "Oh noes"

let handleErrorByReturningOption (input: string) =
    match System.Int32.TryParse(input) with
    | (true,int) -> Some(int)
    | _ -> None

let handleErrorByReturningResult (input: string) =
    match System.Int32.TryParse(input) with
    | (true,int) -> Ok(int)
    | _ -> Error "Could not convert input to integer"

let bind switchFunction twoTrackInput =
    twoTrackInput |> Result.bind switchFunction

let cleanupDisposablesWhenThrowingException (resource: IDisposable) =
    try
        failwith "Oh noes"
    finally
        resource.Dispose()