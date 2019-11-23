module ErrorHandling
open System
open System

let handleErrorByThrowingException() = failwith "Oh noes"

let handleErrorByReturningOption (input: string) =
    try Some (int input)
    with | _ -> None

let handleErrorByReturningResult (input: string) =
    try Ok (int input)
    with | _ -> Error "Could not convert input to integer"

let bind switchFunction twoTrackInput =
    twoTrackInput |> Result.bind switchFunction

let cleanupDisposablesWhenThrowingException (resource: IDisposable) =
    try
        failwith "Oh noes"
    finally
        resource.Dispose()