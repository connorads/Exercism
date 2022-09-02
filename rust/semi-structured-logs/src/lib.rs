/// various log levels
#[derive(Clone, PartialEq, Eq, Debug)]
pub enum LogLevel {
    Info,
    Warning,
    Error,
}
/// primary function for emitting logs
pub fn log(level: LogLevel, message: &str) -> String {
    return match level {
        LogLevel::Info => info(message),
        LogLevel::Warning => warn(message),
        LogLevel::Error => error(message),
    };
}
pub fn info(message: &str) -> String {
    return format!("[INFO]: {}", message);
}
pub fn warn(message: &str) -> String {
    return format!("[WARNING]: {}", message);
}
pub fn error(message: &str) -> String {
    return format!("[ERROR]: {}", message);
}
