import { NextResponse } from "next/server";

export async function POST(
  request: Request,
  { params }: { params: Promise<{ id: string }> }
) {
  try {
    const { id } = await params;
    const bikeId = parseInt(id);

    return NextResponse.json({ message: "Ride ended successfully" });
  } catch (error) {
    console.error("Error ending ride:", error);
    return NextResponse.json(
      { error: "Internal server error", message: "Failed to end ride" },
      { status: 500 }
    );
  }
}
