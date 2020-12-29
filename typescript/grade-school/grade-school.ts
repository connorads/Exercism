export default class GradeSchool {
  constructor(private readonly _roster = new Map<string, string[]>()) {}

  private students = (grade: number): string[] =>
    this._roster.get(String(grade)) || [];

  private addToRoster = (student: string, grade: number): void => {
    this._roster.set(String(grade), [...this.students(grade), student].sort());
  };

  private removeFromRoster = (student: string): void => {
    for (const grade of this._roster.values()) {
      const index = grade.indexOf(student);
      if (index !== -1) grade.splice(index, 1);
    }
  };

  studentRoster = (): Map<string, string[]> =>
    new Map(JSON.parse(JSON.stringify(Array.from(this._roster))));

  addStudent(student: string, grade: number): void {
    this.removeFromRoster(student);
    this.addToRoster(student, grade);
  }

  studentsInGrade = (grade: number): string[] => [...this.students(grade)];
}
